@echo off
cls
md C:\Genoverse
xcopy /s /e  Z:\*.* C:\Genoverse
cd C:\Genoverse
start C:\Genoverse\Genoverse.py
exit