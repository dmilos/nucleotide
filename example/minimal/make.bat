
cd alignment
call %prg_scons% -c
call %prg_scons%
cd ..


cd architecture
call make_all.bat
cd ..

cd alignment
call %prg_scons% -c
call %prg_scons%
cd ..

cd configuration
call %prg_scons% -c
call %prg_scons%
cd ..

cd dialect
call %prg_scons% -c
call %prg_scons%
cd ..


cd encode
call %prg_scons% -c
call %prg_scons%
cd ..

cd configuration
call %prg_scons% -c
call %prg_scons%
cd ..

cd exception
call %prg_scons% -c
call %prg_scons%
cd ..


cd hello
call %prg_scons% -c
call %prg_scons%
cd ..

cd include
call %prg_scons% -c
call %prg_scons%
cd ..

cd package
call %prg_scons% -c
call %prg_scons%
cd ..

cd pdb
call %prg_scons% -c
call %prg_scons%
cd ..

cd rebuild_lazy
call %prg_scons% -c
call %prg_scons%
cd ..

cd rtl
call %prg_scons% -c
call %prg_scons%
cd ..

cd rtti
call %prg_scons% -c
call %prg_scons%
cd ..

cd translator-version
call %prg_scons% -c
call %prg_scons%
cd ..

cd version
call %prg_scons% -c
call %prg_scons%
cd ..

cd warning-return-reference
call %prg_scons% -c
call %prg_scons%
cd ..

cd warning-unused
call %prg_scons% -c
call %prg_scons%
cd ..

pause