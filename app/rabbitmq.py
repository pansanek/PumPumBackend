import json
import traceback
from asyncio import AbstractEventLoop
from aio_pika.abc import AbstractRobustConnection
from aio_pika import connect_robust, IncomingMessage
from app.settings import settings
from app.services.task_creation_service import TaskCreationService


async def process_get_task(msg: IncomingMessage):
    try:
        data = json.loads(msg.body.decode())
        await TaskCreationService.get_task_by_id(data['task_id'])
    except:
        traceback.print_exc()
    finally:
        await msg.ack()

async def consume_tasks(loop: AbstractEventLoop) -> AbstractRobustConnection:
    connection = await connect_robust(settings.amqp_url, loop=loop)
    channel = await connection.channel()

    task_created_queue = await channel.declare_queue('mikhienkov_task_created_queue', durable=True)

    await task_created_queue.consume(process_get_task())
    print('Started RabbitMQ consuming for Task Management...')

    return connection
