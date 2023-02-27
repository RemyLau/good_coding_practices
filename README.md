## TL;DR

- Writing good code improves your productivity and makes your projects more
  maintainable.
- I first show case an example of a spaghetti code and how to turn that into
  a nicely formatted and apppropirately documented piece of code.
- Several strategies are then provided that can help you format your code: tox,
  pre-commit, GitHub actions, LSP.

## Preface

Writing clean, consistently styled, readable, and appropriately doccumented
code are the fundamental keys towards maintainable code-bases / projects.
Doing so can greatly reduces the overhead of re-understanding what your code
does. Ok ok, I understand that you want to have a working version of the code
as fast as you can; so long it's a working piece of code, it's a good piece of
code, isn't it? Well, I'm sure you have encountered the following before. You
finished writing a piece of code that gives you what you want at the moment,
but several days, or even weeks, later, you want something slightly different,
let's say a different input files. But all the sudden, you see some execptions
raised. So you have to go back and read what you have writtent. This, I'm quite
sure, is the time you would appreciate yourself if you've written cleaerly
structured and readablecode...

It is even more so when working in a team of developers or researchers. Being
able to glance through the code of your co-workers and quickly can greately
benefit the team as a whole. Think of writing code not only as a way to
communicate with the computer, but also a way to cmomunicate with your
co-workers.

With that being said, I hope you find this short tutorial useful. Note that
these are only my recommondataions of tools that I find helpful in my
personal development workflow, but **not** the only way to write good code.
Over the years, I have found find writing well structured and readable code
quite delightful. Thus, my sole purpose for this repository is to share some of
these tools that have helped me become a more proficient Python programmer with
you and hope that you find programming more enjoyable.

## Overview

- Turning [spaghetti](src/main_before.py) into nicely structured and
  appropriately documented [code](src/main_after.py).
- Let's set up your virtual assitent for reviewing your code
    - [Tox](tox.ini)
    - [Pre-commit](.pre-commit-config.yaml)
    - [GitHub actions](.github/workflows/tests.yml)
- Powertools!
    - [Neovim+LSP](https://neovim.io/) (my
      [configs](https://github.com/RemyLau/remylau/tree/main/dotfiles/.config/nvim))
    - [Copilot](https://github.com/features/copilot)

## Additional resources

- A blog post by Professor [Charles T. Hoyt](https://github.com/cthoyt) about
  good practices in setting up a development environment for Python packages
  [[link](https://cthoyt.com/2020/06/03/how-to-code-with-me-organization.html)].
  This was the first time I was introdcued to this whole new world of automated
  code quality control.
- A wonderful tutorial by [mCoding](https://www.youtube.com/@mCoding) to set up
  GitHub pre-commit hooks [[link](https://www.youtube.com/watch?v=psjz6rwzMdk)].
  This video helped me set up my first ever pre-commit hooks.
    - BTW, I love **ALL** videos made by mCoding; I can't tell you how many
      advanced Python coding skills I've learned by watching his videos. For
      example, [this](https://www.youtube.com/watch?v=X1PQ7zzltz4) video that
      he explained clearly what `super()` really does and how does the Multi
      Resolution Order work in Python.

### Style guides
- Coding style
    - Google style guide [[link](https://google.github.io/styleguide/pyguide.html)]
    - YAPF [[link](https://github.com/google/yapf)]
    - Black stye [[link](https://black.readthedocs.io)]
- Docstring style
    - Numpy docstring style guide
      [[link](https://numpydoc.readthedocs.io/en/latest/format.html)]
    - Numpy docstring style examples
      [[link](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html)]
    - Google docstring style examples
      [[link](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)]
    - Sphinx docstring examples
      [[link](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html)]
    - Sphinx docstring cheatsheet
      [[link](https://matplotlib.org/sampledoc/cheatsheet.html)]

### Tools
- A curated list of supported `pre-commit` hooks
  [[link](https://pre-commit.com/hooks.html)]
- A curated list of `flake8` extensions
  [[link](https://github.com/DmytroLitvinov/awesome-flake8-extensions)]
- A curated list of Github actions
  [[link](https://github.com/sdras/awesome-actions)]
