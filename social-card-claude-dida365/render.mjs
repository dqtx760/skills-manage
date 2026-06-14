import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import { mkdirSync } from 'fs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const OUTPUT_DIR = join(__dirname, 'output');
mkdirSync(OUTPUT_DIR, { recursive: true });

const POSTERS = [
  { selector: '#xhs-01', name: 'xhs-01-cover.png', width: 1080, height: 1440 },
  { selector: '#xhs-02', name: 'xhs-02-before-after.png', width: 1080, height: 1440 },
  { selector: '#xhs-03', name: 'xhs-03-workflow.png', width: 1080, height: 1440 },
  { selector: '#xhs-04', name: 'xhs-04-evidence.png', width: 1080, height: 1440 },
  { selector: '#xhs-05', name: 'xhs-05-case-study.png', width: 1080, height: 1440 },
  { selector: '#xhs-06', name: 'xhs-06-value.png', width: 1080, height: 1440 },
  { selector: '#xhs-07', name: 'xhs-07-closing.png', width: 1080, height: 1440 },
];

async function render() {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();

  const htmlPath = `file:///${join(__dirname, 'index.html').replace(/\\/g, '/')}`;
  await page.goto(htmlPath, { waitUntil: 'networkidle', timeout: 60000 });

  // Wait for fonts to load
  await page.waitForTimeout(3000);

  // Initialize Lucide icons
  await page.evaluate(() => {
    if (window.lucide && typeof window.lucide.createIcons === 'function') {
      window.lucide.createIcons();
    }
  });
  await page.waitForTimeout(1000);

  for (const poster of POSTERS) {
    const el = await page.$(poster.selector);
    if (!el) {
      console.warn(`Poster not found: ${poster.selector}`);
      continue;
    }
    await el.screenshot({
      path: join(OUTPUT_DIR, poster.name),
      type: 'png',
    });
    console.log(`✓ ${poster.name} (${poster.width}×${poster.height})`);
  }

  await browser.close();
  console.log(`\nAll images saved to: ${OUTPUT_DIR}`);
}

render().catch(err => {
  console.error('Render failed:', err);
  process.exit(1);
});
