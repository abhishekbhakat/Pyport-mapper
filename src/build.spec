a = Analysis(['mapper.py'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             )
pyz = PYZ(a.pure)

options = [('u', None, 'OPTION')]

exe = EXE(pyz,
          a.binaries,
          a.datas,
          options,
          name='Pyportmapper',
          debug=False,
          strip=None,
          upx=True,
          console=False)