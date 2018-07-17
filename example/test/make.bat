cd boost-lexical_cast
call %prg_scons% -c
call %prg_scons%
cd ..

cd boost-thread
call %prg_scons% -c
call %prg_scons%
cd ..

cd invoke
call %prg_scons% -c
call %prg_scons%
cd ..

cd macro
call %prg_scons% -c
call %prg_scons%
cd ..

cd package
call %prg_scons% -c
call %prg_scons%
cd ..

cd python
call %prg_scons% -c
call %prg_scons%
cd ..


cd skip-nuke
call %prg_scons% -c
call %prg_scons%
cd ..

cd include
call %prg_scons% -c
call %prg_scons%
cd ..

pause