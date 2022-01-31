from flask import request
from flask_cors import cross_origin
from DB.querys import verify_content, send_report, fix_content


@cross_origin()
def verify_sentence(_id):
    """ set sentence as `verified`
     require an admin token
     """
    token = request.args.get("token")
    if not token:
        return (
            {"ok": False, "error": "an admin token is required for this action"}, 403
        )
    if verify_content(_id, token):
        return {"ok": True}, 200
    return {"ok": False, "error": "token is invalid"}, 403


@cross_origin()
def report_sentence(_id):
    """ report of sentence content """
    if request.method == 'POST':
        report = send_report(_id)
        if report:
            return {"ok": True, "id reported": _id, "report id": report}, 200
        return {"ok": False}, 400
    return {"ok": False}, 405


@cross_origin()
def review_content(_id):
    """ change the content and verify
    require an admin token
    """
    token = request.args.get("token")
    if not token:
        return (
            {"ok": False, "error": "an admin token is required for this action"}, 403
        )
    new_content = request.data
    if new_content:
        result = fix_content(_id, new_content, token)
        if result:
            return {"ok": True, "new content": result}, 200
        return {"ok": False, "error": "token is invalid"}, 403
    return {"ok": False, "error": "you must to provide new content"}, 400
