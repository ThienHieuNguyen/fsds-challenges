# Installing SQLite on your computer

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/SQLite370.svg/1200px-SQLite370.svg.png)

- 🍏 **MacOS**: The latest version of SQLite always comes **pre-installed within Mac OS**. You don’t have to download or install anything else, it’s located in the directory: `/user/bin/`.

    If for any reason, your Mac hasn’t SQLite installed, run `brew install sqlite3`


- 🐧 **Ubuntu**: The sqlite3 module is part of the standard Python library, so on your machine it should already be installed.

    If for any reason, you need to install it anyway, run:
     ``` bash
    sudo apt-get update
    sudo apt-get install sqlite3 libsqlite3-dev
    ```


- 💠 **Windows**: You have to download `sqlite3` from this link `https://www.sqlite.org/2020/sqlite-tools-win32-x86-3310100.zip`. Unzip it to `C:\sqlite3`, this folder has to contain the `sqlite3` executables and not an unzipped folder. Add `C:\sqlite3` to your Windows environment `Path` (-> if you don't know how to do that, check out [this tutorial](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)).

    To execute `sqlite3` from **Git Bash** run :
    ```bash
    winpty sqlite3
    ```
