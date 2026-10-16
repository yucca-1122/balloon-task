# balloon-task.html から、パソコンでダブルクリックして開ける確認用の preview.html を作る
# - Artifact 用の本体には <!doctype html> などが無いので、前後に足す
# - 風船の型（assets/balloon-shape.webp）は、ファイルを直接開いたときに読めないことがあるので、ページの中に埋め込む
# 使い方: python tools/make_preview.py   （balloon-task フォルダで実行。本体を直したら作り直す）
import base64, os

here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(here, 'balloon-task.html'), encoding='utf-8').read()
shape = base64.b64encode(open(os.path.join(here, 'assets', 'balloon-shape.webp'), 'rb').read()).decode('ascii')
src = src.replace('url("assets/balloon-shape.webp")', 'url("data:image/webp;base64,' + shape + '")')
page = ('<!doctype html><html lang="ja"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>'
        + src + '</body></html>')
out = os.path.join(here, 'preview.html')
open(out, 'w', encoding='utf-8').write(page)
print('作った:', out, '%d KB' % (len(page.encode('utf-8')) // 1024))
