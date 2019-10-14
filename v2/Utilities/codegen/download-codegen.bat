@echo off

SETLOCAL

SET script-path=%~dp0

powershell -Command "(new-object System.Net.WebClient).DownloadFile('http://central.maven.org/maven2/org/openapitools/openapi-generator-cli/4.1.1/openapi-generator-cli-4.1.1.jar', '%script-path%openapi-generator-cli-4.1.1.jar')"

ENDLOCAL