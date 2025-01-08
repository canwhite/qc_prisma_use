#todo，在这里操作prisma
import asyncio
from prisma import Prisma

async def main() -> None:
    prisma = Prisma()
    await prisma.connect()

    # 查询所有用户
    users = await prisma.user.find_many()
    print('所有用户:', users)

    """if not"""
    if not users:
        print('用户数组为空')
    else:
        print(f'用户数组不为空，共有{len(users)}个用户')

    """相当于where email = xxx """
    user = await prisma.user.find_first(
        where={
            'email': 'robert@craigie.dev'
        }
    )
    print('特定用户:', user)

    # 检查用户是否存在，不存在则创建
    if user is None:
        print('用户不存在，正在创建新用户...')
        user = await prisma.user.create(
            data={
                'name': 'Robert',
                'email': 'robert@craigie.dev'
            },
        )
        print('新用户已创建:', user)
    else:
        print('用户已存在:', user)

    """  set age = 20 where name = 'guo'   """
    updated_user = await prisma.user.update(
        where={
            'email': 'robert@craigie.dev'
        },
        data={
            'name': 'Robert Craigie'
        }
    )
    print('用户名已更新:', updated_user)
        

    # 查询关联的帖子
    """join on"""
    posts = await prisma.post.find_many(
        where={
            'author': {
                # 这里的 'is' 类似于 SQL 中的 JOIN ON 条件
                # 用于指定关联模型的条件查询
                # 表示查询 author 关联的 User 模型中 email 为 'robert@craigie.dev' 的帖子
                'is': {
                    'email': 'robert@craigie.dev'
                }
            }
        },
        # include用于指定查询结果中包含的关联模型数据
        include={
            'author': True
        }
    )
    print('用户的帖子:', posts)

    # 检查是否存在帖子，不存在则创建
    if not posts:
        print('没有找到帖子，正在创建新帖子...')
        new_post = await prisma.post.create(
            data={
                'title': '我的第一篇帖子',
                'content': '这是使用Prisma创建的第一个帖子内容',
                'author': {
                    'connect': {
                        'email': 'robert@craigie.dev'
                    }
                }
            }
        )
        print('新帖子已创建:', new_post)
    else:
        print('帖子已存在:', posts)
    

    # 分页查询，字句部分
    paginated_posts = await prisma.post.find_many(
        take=5,  # 每页数量
        skip=0,  # 跳过数量
        order={
            'views': 'desc'  # 按浏览量降序
        }
    )
    print('分页帖子:', paginated_posts)

    # 删除帖子
    # 删除所有浏览量小于10的帖子
    """ 
    try:
        deleted_posts = await prisma.post.delete_many(
            where={
                'views': {
                    'lt': 10  # 删除浏览量小于10的帖子
                }
            }
        )
        print(f'已删除 {deleted_posts} 条帖子')
    except Exception as e:
        print(f'删除帖子时出错: {e}')
    """
    # 删除单条帖子
    try:
        # 获取第一条帖子
        post_to_delete = await prisma.post.find_first()
        
        if post_to_delete:
            # 删除指定ID的帖子
            deleted_post = await prisma.post.delete(
                where={
                    'id': post_to_delete.id
                }
            )
            print(f'已删除帖子 ID: {deleted_post.id}, 标题: {deleted_post.title}')
        else:
            print('没有找到可删除的帖子')
    except Exception as e:
        print(f'删除帖子时出错: {e}')



    await prisma.disconnect()

if __name__ == '__main__':
    asyncio.run(main())

