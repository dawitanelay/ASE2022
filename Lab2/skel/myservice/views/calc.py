from flakon import JsonBlueprint
from flask import Flask, request ,jsonify

calc = JsonBlueprint('calc', __name__)


@calc.route('/sum', methods=['GET'])
def sum():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    result = m
    if n < 0:
        for i in range(abs(n)):
            result -= 1
    else:
        for i in range(n):
            result += 1

    return jsonify({'result':str(result)})

@calc.route('/devide', methods=['GET'])
def devide():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    result = 0
    negativeResult = m > 0 and n < 0 or m < 0 and n > 0
    n = abs(n)
    m = abs(m)

    while ( m-n >= 0):
        m -= n
        result += 1
        result = - result if negativeResult else result
    return jsonify({'result':str(result)})

@calc.route('/multiply', methods=['GET'])
def multiply():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    r=0
    i=0
    while i<abs(n):
        r += abs(m)
        i += 1
    if ((m<0 and n>0) or (m>0 and n<0)):
        result =- r
    else:
            result = r
    return jsonify({'result':str(result)})


@calc.route('/subtract', methods=['GET'])
def subtract():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    r = m
    if n < 0:
        for i in range(abs(n)):
            r +=1
    else:
        for i in range(abs(n)):
            r -=1
    return  jsonify({'result':str(r)}) 
