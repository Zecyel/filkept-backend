from .api import ApiRule

Upload = ApiRule(
    method = 'post',
    param = ['remote_url', 'name', 'description'],
    status = {
        'ok': {
            'status': 'success',
            'hint': '上传成功！'
        },
        'err': {
            'status': 'error',
            'hint': '上传失败'
        }
    },
    token = 'require'
)

List = ApiRule(
    method = 'post',
    param = [],
    status = {
        'ok': {
            'status': 'success',
            'hint': '成功获取电子书列表'
        },
        'err': {
            'status': 'error',
            'hint': '获取失败'
        }
    },
    token = 'require'
)

EbookRule = {
    'Upload': Upload,
    'List': List
}