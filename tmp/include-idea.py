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
             'option' : {    'version10': [ '/folder/directorium/v10' ]
                           , 'version20': [ '/folder/directorium/v20' ]
                           , 'version30': [ '/folder/directorium/v30' ]
                        }
            ,'active': "version20"
        }
    )