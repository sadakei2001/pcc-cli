# -*- coding: utf-8 -*-

import sys
import os
import codecs
import json
import argparse

from requester import Requester
from api import apis

def main():
    # プログラム名
    prog = os.path.basename(sys.argv[0])


    # 共通オプションを環境変数から取得
    url = os.environ.get("PCC_URL")
    access_id = os.environ.get("PCC_ACCESS_ID")
    access_key = os.environ.get("PCC_ACCESS_KEY")


    # コマンドラインオプションのルール設定
    parser = argparse.ArgumentParser(prog=prog, usage=prog + " [command] [options]")
    parser.add_argument("--version", action="version", version="pcc-cli 1.0.0")
    subparsers = parser.add_subparsers(dest="command", metavar="command")

    for _command in apis.commands():
        # コマンドごとのオプション
        subparser = subparsers.add_parser(_command, prog=prog, help="", usage=prog + " " + _command + " [options]")
        apis.get(_command).init_argument(subparser)

        # 共通オプション
        subparser.add_argument("--url", metavar="PCC_URL", required=(url == None))
        subparser.add_argument("--access-id", metavar="PCC_ACCESS_ID", required=(access_id == None))
        subparser.add_argument("--access-key", metavar="PCC_ACCESS_KEY", required=(access_key == None))

    args = parser.parse_args()


    # 共通オプションがコマンドラインで指定されていれば優先して利用する
    if (args.url != None):
        url = args.url

    if (args.access_id != None):
        access_id = args.access_id

    if (args.access_key != None):
        access_key = args.access_key


    # APIを実行
    requester = Requester(url, access_id, access_key)
    response = apis.get(args.command).execute(requester, args)


    # エラーハンドリング
    if (response.get("SUCCESS") == False):
        output(response.get("Message"))
        sys.exit(1)


    # レスポンスを整形して出力
    response_json = json.dumps(response, ensure_ascii=False, indent=4)
    output(response_json)

    sys.exit(0)


def output(message):
    sys.stdout = codecs.getwriter("utf_8")(sys.stdout)
    sys.stdout.write(message)
    sys.stdout.write("\n")
