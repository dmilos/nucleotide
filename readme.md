#Wrap all C++ compilers in to the one.

##Description

  An Scons library which wraps interface of various compilers in to one universal.
  Nucleotide allow us to make Scons files avoiding to explicitly state: platform, compiler, compiler's version.

##Quick example:

  Next line set RTL:
```c++
    settings.accumulate( 'RTL', { 'type': 'static', 'configuration' : 'debug' } )
```
  and replace:
```c++
            if( os.platform == 'win32' ):
                if( retrieve_compiler_name() == 'msvc' ):
                    flag = 'M'
                    if( 'dynamic' == retrieve_RTL_type() ):
                        flag += 'D'
                    if( 'static' == retrieve_RTL_type() ):
                        flag += 'T'
                    if( 'debug' == retrieve_configuration_type() ):
                        flag += 'd'
                    if( 'release' == retrieve_configuration_type() ):
                        pass
                    env.append( CPPFLAGS, [ flag ] )

                if( retrieve_compiler_name() == 'cygwin' ):
                    env.append( LINKFLAGS, "-static" )

                if( retrieve_compiler_name() == 'mingw' ):
                    env.append( LINKFLAGS, "-static" )
            else:
                if( os.platform == 'linux' ):
                    if( retrieve_compiler_name() == 'gcc' ):
                        env.append( LINKFLAGS, "-static" )
            ... ... ... 
```

More details in ./doc/index.html !!!
