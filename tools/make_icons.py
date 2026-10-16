# アプリのアイコン一式を、元の正方形の絵から作る（ChatGPT で描いた「空に浮かぶ珊瑚色の風船」）
# - apple-touch-icon.png（180）… iPhone のホーム画面
# - icon-192.png・icon-512.png … Android のホーム画面など
# - icon-maskable-512.png … Android の丸い切り抜き用。絵を8割に縮め、周りは端の色をのばして空を広げる（ひもの先が欠けないように）
# - favicon-32.png … ブラウザのタブ
# 使い方: python tools/make_icons.py <元の絵のパス>   （balloon-task フォルダで実行）
import os, sys
import numpy as np
from PIL import Image

here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = Image.open(sys.argv[1]).convert('RGB')
if src.width != src.height:
    raise SystemExit('正方形の絵にしてください')
out_dir = os.path.join(here, 'assets', 'icons')
os.makedirs(out_dir, exist_ok=True)

def save(img, name, size):
    im = img.resize((size, size), Image.LANCZOS)
    p = os.path.join(out_dir, name)
    im.save(p, optimize=True)
    print(name, im.size, '%d KB' % (os.path.getsize(p) // 1024))

save(src, 'apple-touch-icon.png', 180)
save(src, 'icon-192.png', 192)
save(src, 'icon-512.png', 512)
save(src, 'favicon-32.png', 32)

# 丸い切り抜き用：8割に縮めて、まわりは端の色をそのままのばす（空のグラデーションは縦方向だけなので、つなぎ目が出ない）
inner = 410
small = np.asarray(src.resize((inner, inner), Image.LANCZOS))
pad = (512 - inner) // 2
big = np.pad(small, ((pad, 512 - inner - pad), (pad, 512 - inner - pad), (0, 0)), mode='edge')
Image.fromarray(big).save(os.path.join(out_dir, 'icon-maskable-512.png'), optimize=True)
print('icon-maskable-512.png', (512, 512), '%d KB' % (os.path.getsize(os.path.join(out_dir, 'icon-maskable-512.png')) // 1024))
