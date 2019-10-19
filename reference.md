# Vim workshop

This is the reference document used in the vim Hacker Tools workshop AY19/20
Semester 1.

Made by Herbert Ilhan Tanujaya, for NUS Hackers.

## Preparation
Install vim

## vim vs emacs
Both are good tools. However, I actually recommend you to use emacs instead.
(Jethro's pretty good at it)

In general, learning a tool like vim or emacs takes a lot of time, but it is
definitely very rewarding if you are going to write a lot of code (or anything
in general, really). Almost all IDEs (Visual Studio Code, Atom, Sublime Text)
have support for vim or emacs keybindings.

Some considerations to choose your tool:
- Knowing someone that uses the tool extensively helps you learn a lot. This is
  applicable in a lot of things as well -- having a good mentor makes you learn
  a lot.
- vim is almost exclusively a text editing tool. You can do a lot of things with
  emacs; it is as if emacs is your operating system.

## vimtutor
`vimtutor` is a command that is typically available in some systems. Try running
`vimtutor` in your system.

If it is not available, we have provided the `vimtutor` file in this repository
for your reference. Just type `vim vimtutor` to open the `vimtutor` file.

## Thinking in vim
You might realise that there is a lot of complicated things you can do with vim.
Basically, the paradigm in vim is to think of each command as a "word". We can
connect each word to a sentence. In the sentences we form, we can substitute
words, and we expect them to do the same.

Remember: operator [number] motion.

Let us open a new file for scratch: you can type `vim` which you can save later
via `:w filename`, or you can open a (possibly nonexistent) file directly via
`vim filename`. For each question, let us guess first what the command does;
afterwards, we verify through our scratchpad.

1. We learnt that `0` moves your cursor to the start of the line. What does `d0`
   do? How about `c0`?
2. What does `cc` do?
3. If you use `W` instead of `w`, you can move into greater distances. Basically,
   with `w`, a word is delimited by most symbols, while with `W`, a word is
   delimited by most whitespaces.

   What does `dW` do? `vW`? `cW`? `2dW`?
4. `b` moves your cursor back one word. What does `db` do? `cb`? How about `B`?
5. Let's say you have a very very long line that spans more than one line in your
   vim buffer. You can go down a line buffer by `gj`. (Try it out in your
   scratchpad; to insert a very long line, I like to use `1000i`, and typing
   'a' in insert mode.)

   What does `gk` do? What does `g0` and `g$` do?

## Some vim workflows
In this section, we are going to try out some workflows that makes using vim
convenient.

### Sorting
Open `dumb.py`. This file does not do much meaningful things; it just prints a
bunch of random things.

One common thing most codebases enforce is some code style via the use of
linting tools. One of them is import sorting. Let us try to sort the imports on
the top of this file (alphabetically).

Use the `dd` and `p` commands to manually sort the imports. For reference, we
want it to be:
```
import fractions
import hashlib
import math
import os
import sys
```

Now let us do it in a faster way. Spam `u` to undo all the way back to the
original file.

1. Use visual to select the import lines. In this case I like to use visual line
instead. You can use visual line by pressing `V` instead of `v`.
2. Press `:`. You should see `:'<,'>` at the bottom of your screen. This means
that whatever you do will be operated only on the lines selected.
3. Type `!sort` and press enter. We pass in whatever we selected to the terminal
utility `sort`.

### Replacing stuff
Open `division.html`. This file is a simple HTML file talking about division.

Notice that in the `body` tag, all the components are using `div`. This is not
so good. Let us replace them with `p` instead.

First of all, let us try using vim's built-in search and replace. You might be
tempted to replace all `div` with `p`. However, the word `division` contains
`div`, and replacing them with `p` changes the word into `pision`. We do not
want to do that. Let us replace `<div>` and `</div>` instead into `<p>` and
`</p>`.

Now, let us try something different. Undo all the way back. Let us search for
the word `div` by typing `/div`. Use `cw` to change it to `p`. Let us now
navigate using `n` or `N`. However, when we change the next occurences, we use
`.` instead of `cw` directly. `.` repeats the previous command - very very
useful!

One last time: let us undo all the way back. Now, instead of searching for
`/div`, we position our cursor into one of the `div` and press `*`. Now only
whole words on the cursor is searched. Very very useful too!

As an aside, if the search highlights some words and you wish to turn them off,
you can type `:nohlsearch` to turn them off. You can use `:noh` as a shortcut.
Even better, you can bind a key into it. More of that later.

### Aligning stuff
Open `trigonometry.tex`. This file is a simple LaTeX file that aims to show a
trigonometric identity.

In the file, you can see some symbols like `&=`. Basically, the `=` is an equal
sign, and the `&` indicates that those symbols after the `&` sign is going to be
aligned in the same vertical line.

Let us aim to make it aligned in our code as well for aesthetics. Let us try to
do it in three ways.

For the first method, let us use vim's built-in indenting method.
1. Use `V` (visual line) to select the two lines that are going to be indented.
2. Press `>` to indent the lines.
3. Do it a few times until all the `&` signs are aligned. Note that you can also
   use numbers like `3>` etc. If you shoot too far, you can always revert it
   via `<`.

That is great for simple indenting, such as normal codebases. However, it can
take quite some time if you wish to indent a lot. Let us discuss another
approach: using visual block.
1. Position your cursor to the first `&` to be indented (line 7).
2. Press Ctrl+V to enter visual block. Visual block allows you to select
   rectangles.
3. Select both `&`s.
4. Press `I` (capital i) to enter insert mode. (Not small i!)
5. Press space a number of times to indent.
6. Press `ESC` to return to normal mode. You'll notice that the second line will
   be automatically indented.

Notice that this flow is similar to Sublime Text's multiple cursors
functionality.

Finally, we are going to try something rather different. This is personally my
own flow.
1. Copy the first line of the equations (line 6): `V` to select the entire line,
   then `y` to copy it.
2. Paste it two times: press `p` twice. (You can also press `2p` if you want,
   though that is not so natural for me.)
3. Block select the two lines of equations after the equal sign. You can do so
   by positioning your cursor at the top `\frac`, and then pressing `Ctrl-V`.
   Afterwards, press `$` to go to the end of the line, then press `j` to go
   down. Your cursor should now select:
   ```
   \frac{1}{2} [(\cos x \cos y - \sin x \sin y) + (\cos x \cos y + \sin x \sin y)] \\
   \frac{1}{2} [\cos (x + y) + \cos (x - y)]
   ```
4. Press `y` to copy that part.
5. Block select the two lines that we have previously copied and pasted, but
   only after the equals sign. This should be lines 7-8 now.
6. Press `p` to paste the previously copied text over the lines.
7. Now, we just need to delete those before the ampersand sign. Block select
   the text before the ampersand `&`.
8. Press `r` to replace, and press ` ` (space) to replace all of them with
   space.
9. Delete the last two lines of the equation (lines 9 to 10).

You may realise that this sequence of commands can be overly complex. That is
fine; every person has different ways of using vim to do it. This just happens
to be the flow that I typically adopt.

The way I am thinking through this is something like:
- Pressing space / indenting is too manual
- Maybe I can just copy the first line to keep the `&=` locations
- Ah, I can replace the left hand side with spaces, and the right hand side with
  the text below, which I can copy.

## Making vim your primary text editor
There is a lot of things to be learnt in vim. However, you do not need to
memorise all commands to be ultra productive. You just need to adopt a subset of
the commands that make you productive enough. (Diminishing returns and all
that.)

In general, this is what I personally do. I think this is applicable to quite
a lot of other tooling stuff.

1. Figure out what you do a lot, but you cannot do it quickly. For example, we
   have not learnt how to scroll down a buffer quickly. We cannot just spam `j`.
   It is too painful!
2. Search (in Google, or ask your friends, etc.) how to do it quickly. For
   example, by this method, we learnt that we can use CTRL-D and CTRL-U to
   scroll down and up quickly.
3. Remember this command, and force yourself to use it every time you encounter
   the problem. When you read/write some code, every time you wish to scroll up
   or down fast, think loudly, "I am going to scroll down, and I am going to
   press CTRL-D for it". Then press CTRL-D.
4. Hopefully, after doing step 3 again and again, you can internalise the
   command you wish to learn. Now repeat to step 1 for any other pain points.

## Using vim as an IDE
vim by itself is not very nice to use. However, we can augment it so that
it can become an IDE like other (heavier) text editors.

vim has some plugin functionality. However, almost no one uses them by itself.
Instead, people usually install plugin managers to make their life easier.
Today, we are going to install `vim-plug`. (There are other alternatives like
`pathogen`, `Vundle`).

1. Google `vim-plug`.
2. Open the repository.
3. Follow the instructions.

Now that we have installed `vim-plug`, let us add our first plugin. You can
configure `vim` settings at this file called `.vimrc`.

1. Type `vim ~/.vimrc` to open the file.
2. Type in `set number` inside.
3. Save and exit.
4. Open vim again and edit stuff. You should now see line numbers.

Now, let us try to install some plugins.

1. Open your vimrc file again. You can actually open `vim`, and do `:e $MYVIMRC`
   now.
2. Type in this block:
   ```vimscript
   call plug#begin()
   Plug 'tpope/vim-sensible'
   Plug 'vim-airline/vim-airline'
   call plug#end()
   ```
3. Save and exit vim.
4. Reopen and run `:PlugInstall`. You should now see that vim is cloning a
   bunch of repositories.
5. Once it is done, exit and open vim.

`vim-sensible` gives you a sane default configuration to start with. This
includes things like showing line number, syntax highlighting, and whatnot.
`vim-airline` gives you a status bar at the bottom. The default is pretty good.

Here are some plugins that makes your vim closer and closer to becoming an IDE.
- `scrooloose/nerdtree` gives you a sidebar to browse files.
- `junegunn/fzf` is a fuzzy finder, so that you can find your files quickly.
- `jiangmiao/auto-pairs` adds the closing pair automatically when you write
  things like open brackets `(`, `[` etc.
- `Shougo/deoplete.nvim` adds (a better) autocompletion.
- `autozimu/LanguageClient-neovim` adds some things like going to definition,
  etc.
- `tpope/vim-surround` allows you to use `S` to add parantheses, etc.

For every language, there are also typically plugins that add syntax
highlighting support and whatnot. For example, you can check
- `derekwyatt/vim-scala`
- `tpope/vim-rails`
- `pangloss/vim-javascript`
- `mxw/vim-jsx`
- `leafgarland/typescript-vim`
- `peitalin/vim-jsx-typescript`
- `rust-lang/rust.vim`

and so on.

There are many vimrc references that you can follow. For example, mine is at
https://github.com/donjar/dotfiles/blob/master/.config/nvim/init.vim. However,
note that I believe for maximal benefit, one should try to repeat the process
I mentioned earlier (looking for pain points and solving them), instead of
blindly copying vimrc files.

## Miscellaneous tips
- A lot of IDEs have vim keybindings. You can even make your browser have
  vim keybindings by using this plugin called Vimium.
- You can show multiple buffers by using `:split` or `:vsplit`, which you can
  shortcut as `:sp` and `:vs`. You can navigate between them by using
  `Ctrl-W Ctrl-W` or `Ctrl-W h` etc.
- The initial learning curve is indeed steep. Do not be discouraged if your
  productivity is halved in the first few months or so. It does pay off very
  well!
