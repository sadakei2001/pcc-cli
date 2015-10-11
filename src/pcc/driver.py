# -*- coding: utf-8 -*-

import sys
import os
import codecs
import json
import argparse.argparse as argparse

from requester import Requester
from api import apis

def main():
    # コマンドラインオプションのルール設定
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="api_name")

    for name in apis.names():
        # コマンドごとのオプション
        subparser = subparsers.add_parser(name)
        apis.get(name).init_argument(subparser)

        # 共通オプション
        subparser.add_argument("--url", help="PCC url (ex. http://localhost/auto-web/)")
        subparser.add_argument("--access-id", help="PCC user access id")
        subparser.add_argument("--access-key", help="PCC user access key")

    args = parser.parse_args()
#    print args


    # 共通オプションの取得
    url = args.url
    access_id = args.access_id
    access_key = args.access_key


    # 共通オプションがコマンドラインで指定されていなければ、環境変数から取得
    if (url == None):
        url = os.environ.get("PCC_URL")

    if (access_id == None):
        access_id = os.environ.get("PCC_ACCESS_ID")

    if (access_key == None):
        access_key = os.environ.get("PCC_ACCESS_KEY")


    # 共通オプションのチェック
    if (url == None):
        print "--url option is required."
        sys.exit(1)

    if (access_id == None):
        print "--access-id option is required."
        sys.exit(1)

    if (access_key == None):
        print "--access-key option is required."
        sys.exit(1)


    # コマンドに対応するAPIモジュールを取得
    api = apis.get(args.api_name)
    if (api == None):
        print args.api_name + " does't exist."
        sys.exit(1)


    # APIを実行
    requester = Requester(url, access_id, access_key)
    response = api.execute(requester, args)


    # レスポンスを整形して出力
    response_json = json.dumps(response, ensure_ascii=False, indent=4)

    sys.stdout = codecs.getwriter("utf_8")(sys.stdout)
    sys.stdout.write(response_json)
    sys.stdout.write("\n")
