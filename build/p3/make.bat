mkdir nucleotide
xcopy /E /Y ..\..\src\nucleotide nucleotide
copy ..\..\license.txt .

set prg_pandoc="c:\Program Files (x86)\Pandoc\pandoc.exe"
%prg_pandoc% --from=markdown --to=rst --output=readme.rst ..\..\readme.md

copy readme.rst readme.txt

%prg_python3% setup.py sdist bdist_wheel

pause
