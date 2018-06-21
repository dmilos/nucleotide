
cd 00_minimal
call %prg_scons% -c
call %prg_scons%
cd ..

cd 01_extend
call %prg_scons% -c
call %prg_scons%
cd ..

cd 02_cpp11
call %prg_scons% -c
call %prg_scons%
cd ..

pause