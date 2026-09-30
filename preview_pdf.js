const puppeteer = require("puppeteer");
const path = require("path");
const fs = require("fs");
(async () => {
  const browser = await puppeteer.launch({ headless: "new", args: ["--no-sandbox"] });
  const page = await browser.newPage();
  await page.setViewport({ width: 1400, height: 900 });
  await page.goto("file:///" + path.resolve(__dirname, "B95-PROJECT-Company-Profile.pdf").replace(/\\/g, "/"), { waitUntil: "networkidle0", timeout: 30000 });
  await new Promise(r => setTimeout(r, 2000));
  fs.writeFileSync(path.resolve(__dirname, "pdf_check.png"), await page.screenshot({ type: "png" }));
  console.log("Done");
  await browser.close();
})();
