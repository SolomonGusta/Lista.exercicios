@echo off
setlocal EnableDelayedExpansion
chcp 65001 >nul

cd /d "%~dp0"
echo Pasta do repositorio: %CD%
echo.

REM [1] Localizar a venv criada pelo aluno (procura qualquer pasta que tenha Scripts\activate.bat)
set "VENV_DIR="
for /d %%D in (*) do (
    if exist "%%~fD\Scripts\activate.bat" (
        set "VENV_DIR=%%~fD"
        goto :found_venv
    )
)

REM Caso o nome da venv tenha sido declarado em um arquivo local (ex: .venv_name ou venv_name.txt)
if exist ".venv_name" (
    set /p CUSTOM_VENV=<".venv_name"
    set "CUSTOM_VENV=!CUSTOM_VENV: =!"
    if not "!CUSTOM_VENV!"=="" if exist "%CD%\!CUSTOM_VENV!\Scripts\activate.bat" (
        set "VENV_DIR=%CD%\!CUSTOM_VENV!"
        goto :found_venv
    )
)

:missing_venv
echo =====================================================================
echo ATENCAO: Nenhuma venv encontrada nesta pasta do repositorio.
echo Como a criacao da venv faz parte do que ja foi visto em aula,
echo o script nao vai cria-la automaticamente.
echo.
echo SOLICITACAO DE AJUDA: Chame o facilitador no terminal para realizar
echo a criacao manual da venv antes de prosseguir.
echo =====================================================================
pause
exit /b 1

:found_venv
echo [OK] venv localizada em: "%VENV_DIR%"
echo.

REM [2] Configurar e instalar Chocolatey portatil (sem acesso de administrador)
set "ChocolateyInstall=%USERPROFILE%\chocoportable"
set "PATH=%ChocolateyInstall%\bin;%PATH%"

if not exist "%ChocolateyInstall%\bin\choco.exe" (
    echo [INFO] Instalando Chocolatey portatil em "%ChocolateyInstall%"...
    mkdir "%ChocolateyInstall%" >nul 2>&1
    powershell -NoProfile -ExecutionPolicy Bypass -Command ^
      "$env:ChocolateyInstall='%ChocolateyInstall%'; [System.Net.ServicePointManager]::SecurityProtocol=[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
    if errorlevel 1 (
        echo [ERRO] Falha ao baixar ou instalar o Chocolatey portatil.
        echo Verifique conexao/proxy da rede institucional ou acione o facilitador.
        pause
        exit /b 1
    )
) else (
    echo [OK] Chocolatey portatil ja presente em "%ChocolateyInstall%".
)

echo.
echo [INFO] Validando prioridade do Chocolatey portatil:
where choco
choco --version
echo.

REM [3] Ativar a venv encontrada e instalar o Selenium nela
echo [INFO] Ativando a venv e instalando selenium...
call "%VENV_DIR%\Scripts\activate.bat"
if errorlevel 1 (
    echo [ERRO] Falha ao ativar a venv em "%VENV_DIR%".
    pause
    exit /b 1
)

python -m pip install --upgrade pip
python -m pip install selenium
if errorlevel 1 (
    echo [ERRO] Falha ao instalar o selenium dentro da venv.
    pause
    exit /b 1
)

echo.
echo [OK] Concluido! Selenium instalado na venv: "%VENV_DIR%"
python -c "import selenium, sys; print('Python:', sys.executable); print('Selenium:', selenium.__version__)"
echo.
pause