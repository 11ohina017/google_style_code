#!/usr/bin/python
# -*- coding: utf-8 -*-
"""���W���[���̐����^�C�g��

     * �\�[�X�R�[�h�̈�Ԏn�߂ɋL�ڂ��邱��
     * import���O�ɋL�ڂ���

Todo:
   TODO���X�g���L��
    * conf.py��``sphinx.ext.todo`` ��L���ɂ��Ȃ��Ǝg�p�ł��Ȃ�
    * conf.py��``todo_include_todos = True``�ɂ��Ȃ��ƕ\������Ȃ�

"""

import json
import inspect

class testClass() :
    """�N���X�̐����^�C�g��

     �N���X�ɂ��Ă̐�����

    Attributes:
        �����̖��O (�����̌^): �����̐���
        �����̖��O (:obj:`�����̌^`): �����̐���.

    """

    def print_test(self, param1, param2) :
        """�֐��̐����^�C�g��

         �֐��ɂ��Ă̐�����

        Args:
            �����̖��O (�����̌^): �����̐���
            �����̖��O (:obj:`�����̌^`, optional): �����̐���.

        Returns:
           �߂�l�̌^: �߂�l�̐��� (�� : True �Ȃ琬��, False �Ȃ玸�s.)

        Raises:
            ��O�̖��O: ��O�̐��� (�� : �������w�肳��Ă��Ȃ��ꍇ�ɔ��� )

        Yields:
           �߂�l�̌^: �߂�l�ɂ��Ă̐���

        Examples:

            �֐��̎g�����ɂ��ċL��

            >>> print_test ("test", "message")
               test message

        Note:
            ���ӎ����Ȃǂ��L��

    """
        print("%s %s" % (param1, param2) )

if __name__ == '__main__':

    test_object = testClass()
    test_object.print_test("test", "message")
    