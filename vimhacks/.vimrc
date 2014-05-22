filetype off
call pathogen#incubate()
call pathogen#helptags()
set foldmethod=indent
set foldlevel=99
filetype plugin on
syntax on
filetype on
filetype plugin indent on
au FileType python set omnifunc=pythoncomplete#Complete
let g:SuperTabDefaultCompletionType = "context"
autocmd FileType html set omnifunc=htmlcomplete#CompleteTags
set laststatus=2
"Automatic vimrc reload"
autocmd! bufwritepost .vimrc source %

"Expanding tab to spaces"
set completeopt=menuone,longest,preview
set shiftwidth=4
set tabstop=4
set expandtab

"Intendation
nnoremap <Tab> >>_
nnoremap <S-Tab> <<_
inoremap <S-Tab> <C-D>
vnoremap <Tab> >gv
vnoremap <S-Tab> <gv
"Removing preview from autocomplete"
autocmd FileType python setlocal completeopt-=preview

"Mapping ctrl-d to save and quit"
:map <C-D> :wq<CR>
:imap <C-D> <ESC><C-D>

"Mapping ctrl-shift-d to quit"
:map <C-S-D> :q!<CR>
:imap <C-S-D> <ESC><C-S-D>

"Mapping ctrl-s to save"
:map <C-Z> :update<CR>
:imap <C-Z> <ESC><C-Z> 

"Mapping ctrl-t to open new tab"
:map <C-T> :tabnew<CR>
:imap <C-T> <ESC><C-T>

"Mapping ctrl-shift-right to move to next tab"
:map <C-S-RIGHT> :tabnext<CR>
:imap <C-S-RIGHT> <ESC><C-S-RIGHT>

"Mapping ctrl-shift-left to move to previous tab"
:map <C-S-LEFT> :tabprevious<CR>
:imap <C-S-LEFT> <ESC><C-S-LEFT>

"Mapping ctrl-q to save and quit all "
:map <C-Q> :wqa!<CR>
:imap <C-Q> <ESC><C-Q>

"Mapping ctrl-shift-q to quit all without saving"
:map <C-S-Q> :qa!<CR>
:imap <C-S-Q> <ESC><C-S-Q>

"Mapping ctrl-w to close tab"
:map <C-W> :tabclose<CR>
:imap <C-W> <ESC><C-W>


"Mapping ctrl-shift-r to format indentaion"
:map <C-S-R> :normal gg=G<CR>
:imap <C-S-R> <ESC><C-S-R>


:map <silent><C-S-D> :!xinput set-prop 11 "Device Enabled" 1<CR><CR>
:map <silent><C-S-A> :!xinput set-prop 11 "Device Enabled" 0<CR><CR>
"Displaying Line Numbers"
:set number
set smartindent

set pastetoggle=<F2>
"cursor down/up existing lines
"imap <S-Down> _<Esc>mz:set ve=all<CR>i<Down>_<Esc>my`zi<Del><Esc>:set ve=<CR>`yi<Del>
"imap <S-Up> _<Esc>mz:set ve=all<CR>i<Up>_<Esc>my`zi<Del><Esc>:set ve=<CR>`yi<Del>
"cursor down with a new line
"imap <S-CR> _<Esc>mz:set ve=all<CR>o<C-o>`z<Down>_<Esc>my`zi<Del><Esc>:set ve=<CR>`yi<Del>
"noremap <silent> <Leader>w :call ToggleWrap()<CR>
    "setlocal wrap linebreak nolist
    "set virtualedit=
    "setlocal display+=lastline
    "noremap  <buffer> <silent> <Up>   gk
    "noremap  <buffer> <silent> <Down> gj
    "noremap  <buffer> <silent> <Home> g<Home>
    "noremap  <buffer> <silent> <End>  g<End>
    "inoremap <buffer> <silent> <Up>   <C-o><UP>
    "inoremap <buffer> <silent> <Down> <C-o><DOWN>
    "inoremap <buffer> <silent> <Home> <C-o>g<Home>
    "inoremap <buffer> <silent> <End>  <C-o>g<End>
    "set whichwrap+=<,>,h,l,[,]

    "set rtp+=$HOME/.local/lib/python2.7/site-packages/powerline/bindings/vim/

"NerdTree to Control-F
set autochdir
let NERDTreeChDirMode=1
nnoremap <leader>n :NERDTree .<CR>
noremap <C-F> :NERDTreeToggle<CR>
set nofoldenable



"Setting <F5> to run python script
autocmd BufRead *.py set makeprg=python\ -c\ \"import\ py_compile,sys;\ sys.stderr=sys.stdout;\ py_compile.compile(r'%')\"
autocmd BufRead *.py set efm=%C\ %.%#,%A\ \ File\ \"%f\"\\,\ line\ %l%.%#,%Z%[%^\ ]%\\@=%m
autocmd BufRead *.py nmap <F5> :!python %<CR>

" Always show statusline
set laststatus=2

" Use 256 colours (Use this setting only if your terminal supports 256 colours)
set t_Co=256

"Use System Keyboard
set clipboard=unnamedplus


