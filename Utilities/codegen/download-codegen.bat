@echo off

SETLOCAL

SET script-path=%~dp0

powershell -Command "(new-object System.Net.WebClient).DownloadFile('http://insecure.repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/4.2.2/openapi-generator-cli-4.2.2.jar', '%script-path%openapi-generator-cli-4.2.2.jar')"

ENDLOCAL