# tegetege_darts_system

Overview

家でダーツする時に、O1とかカウントアップとか、カウントしてくれるプログラム
This system is just darts counting system for playing at home.

## このアプリを起動する方法
  1. `tegetege_darts_system/`で次のコマンドを利用してコントロールシステムを起動  
    `python control_sys.py`
  1. `tegetege_darts_system/App/electron`で次のコマンドを利用してElectronアプリを起動  
    `npm run start`
    


## 注意事項
(CAUTION!)file(control_sys.py) is For Docker. 
If you do this APP on your local, please swap this file
with './stact/control_sys_for_p.py'.
Not Available due to differences in behavior between 
'python on local' and 'do python APP on Docker'.

(注意!) control_sys.pyはDocker上で稼働する用のコードです。
ローカル環境で利用する場合は、'./stact/control_sys_for_p.py'
とファイルを入れ替えてください。
ローカル環境のpythonとDocker環境のpythonについての挙動の違いによって、
エラーが出てしまいます。
具体的には、このファイル内zero_one_game()関数のresult['score_board']に
関する部分の挙動が異なります。
ローカル環境ではHTMLファイルのフォームから受け取る数値が全てlist内に入ってしまいます。
しかし、Docker環境ではlistにはならず、そのままvalueとして認識されています。
原因がわからず、根本的な解決には至ってはいませんが、そのまま公開させていただきます。
