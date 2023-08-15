import unittest
from functools import wraps


def CustomSkip(func):
    """针对当前用例失败后，后续用例停止执行的装饰器"""

    @wraps(func)
    def wrappend(self):
        if self._outcome.result.failures or self._outcome.result.errors:
            raise unittest.SkipTest(func.__name__, self._outcome.result.failures[0][0]._testMethodName)
        func(self)

    return wrappend


def skip_dependon(depend=""):
    """
    存在依赖关系的用例，依赖用例失败，则被依赖用例跳过执行
    :param depend: 依赖的用例函数名，默认为空
    :return: wraper_func
    """

    def wraper_func(test_func):
        @wraps(test_func)  # @wraps：避免被装饰函数自身的信息丢失
        def inner_func(self):
            if depend == test_func.__name__:
                raise ValueError("{} cannot depend on itself".format(depend))
            failures = str([fail[0] for fail in self._outcome.result.failures])
            errors = str([error[0] for error in self._outcome.result.errors])
            skipped = str([error[0] for error in self._outcome.result.skipped])
            flag = (depend in failures) or (depend in errors) or (depend in skipped)
            if failures.find(depend) != -1:
                # 输出结果 [<__main__.TestDemo testMethod=test_login>]
                # 如果依赖的用例名在failures中，则判定为失败，以下两种情况同理
                # find()方法：查找子字符串，若找到返回从0开始的下标值，若找不到返回 - 1
                test = unittest.skipIf(flag, "{} failed".format(depend))(test_func)
            elif errors.find(depend) != -1:
                test = unittest.skipIf(flag, "{} error".format(depend))(test_func)
            elif skipped.find(depend) != -1:
                test = unittest.skipIf(flag, "{} skipped".format(depend))(test_func)
            else:
                test = test_func
            return test(self)

        return inner_func

    return wraper_func
