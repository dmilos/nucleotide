mkdir nucleotide
xcopy /E /Y ..\src\nucleotide nucleotide
copy ..\license.txt .

call md2rst.bat

%prg_python% setup.py sdist
@rem %prg_python% setup.py egg_info
@rem %prg_python% setup.py bdist_wheel

pause
