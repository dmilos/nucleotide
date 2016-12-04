mkdir nucleotide
xcopy /E /Y ..\src\nucleotide nucleotide
copy ..\license.txt .

call md2rst.bat

copy readme.rst readme.txt

@rem %prg_python% setup.py sdist -o
%prg_python% setup.py sdist --formats=gztar,zip
@rem %prg_python% setup.py egg_info
@rem %prg_python% setup.py bdist_wheel

pause
