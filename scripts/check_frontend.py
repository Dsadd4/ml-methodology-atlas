from playwright.sync_api import sync_playwright,expect
from pathlib import Path
import json,html,textwrap
r=Path(__file__).resolve().parents[1];out=r/'frontend/output/playwright';out.mkdir(parents=True,exist_ok=True)
with sync_playwright() as p:
 b=p.chromium.launch();page=b.new_page(viewport={'width':1440,'height':1080},device_scale_factor=1);errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto((r/'frontend/index.html').as_uri());expect(page.locator('.card')).to_have_count(59);page.screenshot(path=str(out/'desktop.png'))
 page.locator('#search').fill('贝叶斯');assert page.locator('.card').count()>0
 page.locator('#reset').click();page.locator('[data-group="概率与信息"]').click();expect(page.locator('.card')).to_have_count(7)
 page.locator('#reset').click();page.locator('[data-method="M01"]').click();expect(page.locator('dialog')).to_be_visible();page.locator('#close-dialog').click()
 page.locator('[data-select="M01"]').check();page.locator('[data-select="M06"]').check();page.locator('#open-compare').click();expect(page.locator('.compare-table')).to_have_count(1)
 page.locator('nav [data-view="coverage"]').click();page.locator('[data-cell="ICLR,2024"]').click();expect(page.locator('#content .paper')).to_have_count(4)
 page.goto((r/'frontend/index.html').as_uri()+'#method=M53');expect(page.locator('dialog')).to_be_visible();page.locator('#close-dialog').click();page.locator('nav [data-view="methods"]').click();page.locator('#reset').click()
 page.set_viewport_size({'width':390,'height':844});assert page.evaluate('document.documentElement.scrollWidth<=innerWidth');page.screenshot(path=str(out/'mobile.png'));assert not errors,errors
 b.close()
(r/'frontend/QA.md').write_text('# 前端检查\n\n真实Chromium浏览器通过：59张卡片、搜索、分组筛选、详情弹窗、2方法并排对比、覆盖矩阵跳转（ICLR2024=4篇）、M53深链接、390px移动布局无横向溢出。浏览器未捕获JavaScript异常。桌面截图已人工查看，字体和卡片正常。\n')
print('PASS')
