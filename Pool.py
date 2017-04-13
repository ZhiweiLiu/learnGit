from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print('Run task %s (%s)...' % (name,os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ =='__main__':
	print('Parent process %s' % os.getpid())
	p = Pool(4)
	for i in range(10):
		p.apply_async(long_time_task, args=(i,))
	print('Waiting for all subprocesses done...')
	p.close()
	p.join()
	print('All subprocesses done')

# 通过Pool（）方法创建进程池，然后让进程池中的每个进程独立执行任务
# 对Pool对象调用join（）方法会等待所有子进程执行完毕，调用join（）之前先调用close（）
# 调用close（）之后就不能创建Process了
# Pool的默认大小时CPU的核心数量
# 