mkdir nucleotide
xcopy /E /Y ..\src\nucleotide nucleotide
copy ..\license.txt .
copy ..\readme.md readme.txt

%prg_python% setup.py sdist
@rem %prg_python% setup.py bdist_wheel

pause
