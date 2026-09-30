const puppeteer = require("puppeteer");
const { PDFDocument } = require("pdf-lib");
const http = require("http");
const fs = require("fs");
const path = require("path");

// ── Static HTTP Server ────────────────────────────────────────────────────────
function startServer(root, port) {
  const mime = {
    ".html": "text/html", ".css": "text/css", ".js": "application/javascript",
    ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
    ".svg": "image/svg+xml", ".woff": "font/woff", ".woff2": "font/woff2",
    ".ttf": "font/ttf", ".ico": "image/x-icon"
  };
  const server = http.createServer((req, res) => {
    const filePath = path.join(root, decodeURIComponent(req.url.split("?")[0]));
    const ext = path.extname(filePath).toLowerCase();
    fs.readFile(filePath, (err, data) => {
      if (err) { res.writeHead(404); res.end("Not Found"); return; }
      res.writeHead(200, { "Content-Type": mime[ext] || "application/octet-stream" });
      res.end(data);
    });
  });
  return new Promise(resolve => server.listen(port, "127.0.0.1", () => resolve(server)));
}

// ── Main PDF Generation Routine ───────────────────────────────────────────────
(async () => {
  const PORT = 9171;
  const ROOT = __dirname;

  console.log("=== B95 PROJECT — Vector A4 Portrait PDF Generator ===\n");
  console.log(`Starting local server on http://127.0.0.1:${PORT}...`);
  const server = await startServer(ROOT, PORT);
  console.log("✓ Server running.\n");

  const browser = await puppeteer.launch({
    headless: "new",
    args: [
      "--no-sandbox",
      "--disable-setuid-sandbox",
      "--font-render-hinting=none",
      "--disable-gpu",
      "--hide-scrollbars",
      "--enable-font-antialiasing",
      "--force-color-profile=srgb"
    ]
  });

  const page = await browser.newPage();
  // 1200px coordinate space matching desktop design
  await page.setViewport({ width: 1200, height: 900, deviceScaleFactor: 1 });

  const url = `http://127.0.0.1:${PORT}/index.html`;
  console.log("Loading:", url);

  // Wait for full network idle to ensure all fonts/images are loaded
  await page.goto(url, { waitUntil: "networkidle0", timeout: 60000 });

  // Explicitly wait for all fonts to be ready
  const fontsLoaded = await page.evaluate(async () => {
    await document.fonts.ready;
    const fontList = [];
    document.fonts.forEach(f => fontList.push(`${f.family} ${f.weight}: ${f.status}`));
    return fontList;
  });
  console.log("✓ Fonts status:");
  fontsLoaded.forEach(f => console.log("  -", f));

  // Extra wait to ensure all resources rendered
  await new Promise(r => setTimeout(r, 3000));
  console.log("✓ Page and fonts loaded.\n");

  // Switch to print media — triggers @media print rules in styles.css
  await page.emulateMediaType("print");
  await new Promise(r => setTimeout(r, 1000));

  console.log("Rendering vector A4 portrait PDF...");

  // A4 portrait dimensions: 210mm x 297mm
  // Scale factor: 793.7px / 1200px = 0.6614173
  const pdfBuffer = await page.pdf({
    format: "A4",
    landscape: false,
    scale: 0.6614173,
    printBackground: true,
    margin: { top: 0, right: 0, bottom: 0, left: 0 },
    preferCSSPageSize: false,
    displayHeaderFooter: false,
    timeout: 120000
  });

  await browser.close();
  server.close();

  // Validate PDF with pdf-lib
  const checkDoc = await PDFDocument.load(pdfBuffer);
  const pageCount = checkDoc.getPageCount();
  const p0 = checkDoc.getPage(0).getSize();

  const outPath = path.resolve(__dirname, "B95-PROJECT-Company-Profile.pdf");
  fs.writeFileSync(outPath, pdfBuffer);

  const sizeMB = (pdfBuffer.length / (1024 * 1024)).toFixed(2);
  console.log(`\n${"=".repeat(56)}`);
  console.log(`✅  PDF successfully generated: ${outPath}`);
  console.log(`    Format : A4 Portrait (210 × 297 mm)`);
  console.log(`    Pages  : ${pageCount} pages (01/05 to 05/05)`);
  console.log(`    Page 1 : ${Math.round(p0.width)} × ${Math.round(p0.height)} pt`);
  console.log(`    Size   : ${sizeMB} MB (Vector quality)`);
  console.log(`${"=".repeat(56)}`);
})();
