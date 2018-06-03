settings.accumulate(
    'include-single',
        {
         "/what/ever"
        }
    )

settings.accumulate(
    'include-list', # same as 'include'
          [ "/what/ever01", "/what/ever02" ]
    )

settings.accumulate(
    'include-switch',
        {
             'option' : {    'version10': [ '/folder/directorium0/v10', '/folder/directorium1/v10' ]
                           , 'version20': [ '/folder/directorium0/v20', '/folder/directorium1/v10' ]
                           , 'version30': [ '/folder/directorium0/v30', '/folder/directorium1/v10' ]
                        }
            ,'active' : "version20"
            ,'default': "version10"
        }
    )

