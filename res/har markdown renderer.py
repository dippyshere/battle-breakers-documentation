"""
Copyright 2023 Dippyshere
https://github.com/Dippyshere/battle-breakers-documentation

generates a bunch of markdown files for each request in the HAR file
the markdown files are generated in a directory structure that matches the URL, e.g.:
https://www.example.com/foo/bar/baz
would be placed in:
docs/example.com/foo/bar/baz.md

the markdown files contain the following (if its present in the HAR file's entry):

- the URL
- the request method, path, and version
- query string
- request cookies
- request headers
- request body
- response status code
- response cookies
- response headers
- response body
"""
import base64
import json
import os
import re
import sys
import http
import urllib.parse

# this is just for escaping markdown chars inside some f strings
escaped_pipe = "\|"
escaped_star = "\*"


def main():
    """
    main function
    """
    if len(sys.argv) != 2:
        print("usage: {sys.argv[0]} <har file>")
        sys.exit(1)

    with open(sys.argv[1], encoding='utf-8') as f:
        har = json.load(f)

    with open("res/overrides.json", encoding='utf-8') as f:
        overrides = json.load(f)

    for entry in har["log"]["entries"]:
        url = entry["request"]["url"]
        if "<unconfigured>" in url:  # redundant
            continue
        if "ol.epicgames.com" not in url:  # there may be others, but the game client only ever really needs this
            continue
        if "wss" in url:
            continue
        filename = f"{url.split('/')[-1].split('?')[0][:100]}.md"
        method = entry["request"]["method"]
        http_version = entry["request"]["httpVersion"]
        path = re.match(r"https?://([^/]+)(.*)", url).groups()[1]
        description = ""

        try:
            query_string = entry["request"]["queryString"]
        except:
            query_string = []
        if query_string:
            query_string = "\n### Query String\n\n| Name | Value |\n|---|---|\n" + "\n".join(
                f"| {param['name']} | {param['value'].replace('|', escaped_pipe)} |" for param in query_string
            )
        else:
            query_string = ""

        try:
            request_cookies = entry["response"]["cookies"]
        except:
            request_cookies = []
        if request_cookies:
            request_cookies = "\n### Request Cookies\n\n| Name | Value |\n|---|---|\n" + "\n".join(
                f"| {cookie['name']} | {cookie['value']} |" for cookie in request_cookies
            )
        else:
            request_cookies = ""

        try:
            request_headers = entry["request"]["headers"]
        except:
            request_headers = []
        if request_headers:
            request_headers = "\n### Request Headers\n\n| Name | Value |\n|---|---|\n" + "\n".join(
                f"| {header['name']} | {header['value'].replace('*', escaped_star)} |" for header in request_headers
            )
        else:
            request_headers = ""
        try:
            post_data = entry["request"]["postData"]
        except:
            post_data = {}
        if post_data:
            try:
                mime_type = post_data["mimeType"]
                try:
                    if post_data["encoding"] == "base64":
                        post_data["text"] = base64.b64decode(post_data["text"]).decode("utf-8")
                except:
                    pass
                if "application/x-www-form-urlencoded" in mime_type:
                    params = post_data["params"]
                    if params:
                        post_data = "\n### Request Body\n\n| Name | Value |\n|---|---|\n" + "\n".join(
                            f"| {param['name']} | {param['value']} |" for param in params
                        )
                    else:
                        post_data = ""
                elif "application/json" in mime_type:
                    post_data = "\n### Request Body\n\n```json\n" + json.dumps(json.loads(post_data["text"]),
                                                                               indent=2) + "\n```"
                elif "text/plain" in mime_type:
                    post_data = "\n### Request Body\n\n```text\n" + post_data["text"] + "\n```"
                elif "text/html" in mime_type:
                    post_data = "\n### Request Body\n\n```html\n" + post_data["text"] + "\n```"
                elif "application/octet-stream" in mime_type:
                    post_data = "\n### Request Body\n\n```text\n" + post_data["text"] + "\n```"
                elif "multipart/form-data" in mime_type:
                    post_data = "\n### Request Body\n\n```text\n" + post_data["text"] + "\n```"
                elif "application/xml" in mime_type:
                    post_data = "\n### Request Body\n\n```xml\n" + post_data["text"] + "\n```"
                elif "text/xml" in mime_type:
                    post_data = "\n### Request Body\n\n```xml\n" + post_data["text"] + "\n```"
                else:
                    post_data = "\n### Request Body\n\n```text\n" + post_data["text"] + "\n```"
            except:
                post_data = ""
        else:
            post_data = ""

        response_status = entry["response"]["status"]

        try:
            response_cookies = entry["response"]["cookies"]
        except:
            response_cookies = []
        if response_cookies:
            response_cookies = "\n### Response Cookies\n\n| Name | Value |\n|---|---|\n" + "\n".join(
                f"| {cookie['name']} | {cookie['value']} |" for cookie in response_cookies
            )
        else:
            response_cookies = ""

        try:
            response_headers = entry["response"]["headers"]
        except:
            response_headers = []
        if response_headers:
            response_headers = "\n### Response Headers\n\n| Name | Value |\n|---|---|\n" + "\n".join(
                f"| {header['name']} | {header['value'].replace('*', escaped_star)} |" for header in response_headers
            )
        else:
            response_headers = ""
        try:
            response_content = entry["response"]["content"]
        except:
            response_content = {}
        if response_content:
            try:
                mime_type = response_content["mimeType"]
                try:
                    if response_content["encoding"] == "base64":
                        response_content["text"] = base64.b64decode(response_content["text"]).decode("utf-8")
                except:
                    pass
                if "application/x-www-form-urlencoded" in mime_type:
                    params = response_content["params"]
                    if params:
                        response_content = "\n### Response Body\n\n| Name | Value |\n|---|---|\n" + "\n".join(
                            f"| {param['name']} | {param['value']} |" for param in params
                        )
                    else:
                        response_content = ""
                elif "application/json" in mime_type:
                    response_content = "\n### Response Body\n\n```json\n" + json.dumps(
                        json.loads(response_content["text"]), indent=2) + "\n```"
                elif "text/plain" in mime_type:
                    response_content = "\n### Response Body\n\n```text\n" + response_content["text"] + "\n```"
                elif "text/html" in mime_type:
                    response_content = "\n### Response Body\n\n```html\n" + response_content["text"] + "\n```"
                elif "application/octet-stream" in mime_type:
                    response_content = "\n### Response Body\n\n```text\n" + response_content["text"] + "\n```"
                elif "multipart/form-data" in mime_type:
                    response_content = "\n### Response Body\n\n```text\n" + response_content["text"] + "\n```"
                elif "application/xml" in mime_type:
                    response_content = "\n### Response Body\n\n```xml\n" + response_content["text"] + "\n```"
                elif "text/xml" in mime_type:
                    response_content = "\n### Response Body\n\n```xml\n" + response_content["text"] + "\n```"
                else:
                    response_content = "\n### Response Body\n\n```text\n" + response_content["text"] + "\n```"
                try:
                    if entry["response"]["content"]["encoding"] == "base64":
                        response_content += "\n\n*Response body was encoded in base64*"
                except:
                    pass
            except:
                response_content = ""
        else:
            response_content = ""
        try:
            heading = url.split('/')[-1].split('?')[0][0].upper() + urllib.parse.unquote(url.split('/')[-1].split('?')[0][1:])
        except:
            heading = url
        for override_target, override in overrides.items():
            if override_target == url:
                for override_key, override_value in override.items():
                    if override_key == "url":
                        url = override_value
                    elif override_key == "description":
                        description = override_value
                    elif override_key == "method":
                        method = override_value
                    elif override_key == "path":
                        path = override_value
                    elif override_key == "http_version":
                        http_version = override_value
                    elif override_key == "query_string":
                        query_string = override_value
                    elif override_key == "request_cookies":
                        request_cookies = override_value
                    elif override_key == "request_headers":
                        request_headers = override_value
                    elif override_key == "post_data":
                        post_data = override_value
                    elif override_key == "response_status":
                        response_status = override_value
                    elif override_key == "response_cookies":
                        response_cookies = override_value
                    elif override_key == "response_headers":
                        response_headers = override_value
                    elif override_key == "response_content":
                        response_content = override_value
                    elif override_key == "heading":
                        heading = override_value

        text = f"""# {heading}

#####

*{url}*

{description}

___

## Request

```http request
{method} {path} {http_version}
```
{query_string}

{request_cookies}

{request_headers}

{post_data}

___

## Response

#### Status: {response_status} {http.HTTPStatus(int(response_status)).phrase if int(response_status) != 0 else 'EXCEPTION'}

{response_cookies}

{response_headers}

{response_content}

___

{bytes.fromhex("23232323232320546869732066696C65207761732063726561746564206279205B646970707973686572655D2868747470733A2F2F6769746875622E636F6D2F646970707973686572652920666F72205B426174746C6520427265616B65727320446F63756D656E746174696F6E5D2868747470733A2F2F6769746875622E636F6D2F646970707973686572652F626174746C652D627265616B6572732D646F63756D656E746174696F6E29").decode('utf-8')}
"""
        # # if the eg1 token is inside a codeblock, replace the token with token
        # text = re.sub(r'```(.*?)```', lambda m: re.sub(r'eg1~[0-9a-zA-Z_-]*\.[0-9a-zA-Z_-]*\.[0-9a-zA-Z_-]*', 'eg1~token', m.group(1)), text, flags=re.DOTALL)
        text = re.sub(r'[eE]g1~[0-9a-zA-Z_-]*\.[0-9a-zA-Z_-]*\.[0-9a-zA-Z_-]*', 'eg1~token...', text)
        text = text.replace('| bearer eg1~token... |', '| bearer [eg1~token](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/eg1.md) |')
        text = text.replace('| basic M2NmNzhjZDNiMDBiNDM5YTg3NTVhODc4YjE2MGM3YWQ6YjM4M2UwZjQtZjBjYy00ZDE0LTk5ZTMtODEzYzMzZmMxZTlk |', '| basic [M2NmNzhjZDNiMDBiNDM5YTg3NTVhODc4YjE2MGM3YWQ6YjM4M2UwZjQtZjBjYy00ZDE0LTk5ZTMtODEzYzMzZmMxZTlk](https://github.com/dippyshere/battle-breakers-documentation/blob/master/docs/common/tokens/wexclient.md) |')
        directory = os.getcwd() + "/docs/" + re.sub(r"https?://|([^/]+$)", "", url)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # if os.path.exists(directory + "/" + filename):
        #     continue
        with open(directory + "/" + filename, "w", encoding='utf-8') as f:
            f.write(text)


if __name__ == "__main__":
    main()
