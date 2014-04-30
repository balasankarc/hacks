function Sr()
    %s/Note: .*//g
    %s/Subscribe Me//g
    %s/.*msonesubs,.*//g
    %s/.*([0-9].*//g
    %s/Regards.*//g
    %s/Blogger.*//g
    %s/.*|//g
    %s/\n\n//g
    %s/ //g
endfunction
