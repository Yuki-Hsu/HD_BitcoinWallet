# -*- mode: python -*-

block_cipher = None


a = Analysis(['HD_bitcoinwallet.py'],
             pathex=['C:\\Users\\A1718\\Desktop\\coding2\\新建文件夹'],
             binaries=[],
             datas=[('bitcoin\english.txt','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='HD_bitcoinwallet',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='bitbug_favicon.ico')
