'''
Created on 22 Jan 2013

@author: jhkwakkel
'''
import random
import numpy as np

from callbacks import DefaultCallback
from uncertainties import ParameterUncertainty
from expWorkbench import Outcome, EMAlogging

def test_callback_initalization():
    
    # let's add some uncertainties to this
    uncs = [ParameterUncertainty((0,1), "a"),
           ParameterUncertainty((0,1), "b")]
    outcomes = [Outcome("test", time=True)]
    callback = DefaultCallback(uncs, outcomes, nr_experiments=100)
    return callback

def test_callback_store_results():
    nr_experiments = 3
    uncs = [ParameterUncertainty((0,1), "a"),
           ParameterUncertainty((0,1), "b")]
    outcomes = [Outcome("test", time=True)]
    case = {unc.name:random.random() for unc in uncs}
    policy = {'name':'none'}
    name = "test"

    # case 1 scalar shape = (1)
    EMAlogging.debug('----------- case 1 -----------')
    callback = DefaultCallback(uncs, outcomes, nr_experiments=nr_experiments)
    result = {outcomes[0].name: 1}
    callback(case, policy, name, result)
    
    results = callback.get_results()
    for key, value in results[1].iteritems():
        EMAlogging.debug("\n" + str(key) + "\n" + str(value))

    # case 2 time series shape = (1, nr_time_steps)
    EMAlogging.debug('----------- case 2 -----------')
    callback = DefaultCallback(uncs, outcomes, nr_experiments=nr_experiments)
    result = {outcomes[0].name: np.random.rand(10)}
    callback(case, policy, name, result)
    
    results = callback.get_results()
    for key, value in results[1].iteritems():
        EMAlogging.debug("\n" + str(key) + "\n" + str(value))


    # case 2 maps etc. shape = (x,y)
    EMAlogging.debug('----------- case 3 -----------')
    callback = DefaultCallback(uncs, outcomes, nr_experiments=nr_experiments)
    result = {outcomes[0].name: np.random.rand(2,2)}
    callback(case, policy, name, result)
    
    results = callback.get_results()
    for key, value in results[1].iteritems():
        EMAlogging.debug("\n" + str(key) + "\n" + str(value))


def test_callback_call_intersection():
    nr_experiments = 10
    uncs = [ParameterUncertainty((0,1), "a"),
           ParameterUncertainty((0,1), "b")]
    outcomes = [Outcome("test", time=True)]
    callback = DefaultCallback(uncs, outcomes, nr_experiments=nr_experiments)
    
    policy = {"name": "none"}
    name = "test"
    
    for i in range(nr_experiments):
        case = {unc.name: random.random()for unc in uncs}
        result = {outcome.name: np.random.rand(100) for outcome in outcomes}
    
        callback(case, policy, name, result)

def test_callback_call_union():
    # there are actually 3 cases that should be tested here
    # union unc, intersection outcomes
    # intersection unc, union outcomes
    # union unc, union outcomes
    
    # case 1 union unc, intersection outcomes
#    EMAlogging.debug('----------- case 1 -----------')
#    nr_experiments = 10
#    uncs = [ParameterUncertainty((0,1), "a"),
#           ParameterUncertainty((0,1), "b")]
#    outcomes = [Outcome("test", time=True)]
#    callback = DefaultCallback(uncs, outcomes, nr_experiments=nr_experiments)
#    
#    policy = {"name": "none"}
#    name = "test"
#    
#    for i in range(nr_experiments):
#        if i % 2 == 0:
#            case = {uncs[0].name: np.random.rand(1)}
#        else: 
#            case = {uncs[1].name: np.random.rand(1)}
#        result = {outcome.name: np.random.rand(10) for outcome in outcomes}
#    
#        callback(case, policy, name, result)
#    
#    results = callback.get_results()
#    EMAlogging.debug("\n"+str(results[0]))

    
    EMAlogging.debug('----------- case 2 -----------')
#    nr_experiments = 10
#    uncs = [ParameterUncertainty((0,1), "a"),
#           ParameterUncertainty((0,1), "b")]
#    outcomes = [Outcome("test 1", time=True), 
#                Outcome("test 2", time=True)]
#    callback = DefaultCallback(uncs, outcomes, nr_experiments=nr_experiments)
#    
#    policy = {"name": "none"}
#    name = "test"
#    
#    for i in range(nr_experiments):
#        case = {unc.name: random.random()for unc in uncs}
#        if i % 2 == 0:
#            result = {outcomes[0].name: np.random.rand(10)}
#        else: 
#            result = {outcomes[1].name: np.random.rand(10)}
#    
#        callback(case, policy, name, result)
#    


  
    EMAlogging.debug('----------- case 3 -----------')
    nr_experiments = 10
    uncs = [ParameterUncertainty((0,1), "a"),
           ParameterUncertainty((0,1), "b")]
    outcomes = [Outcome("test 1", time=True), 
                Outcome("test 2", time=True)]
    callback = DefaultCallback(uncs, outcomes, nr_experiments=nr_experiments)
    
    policy = {"name": "none"}
    name = "test"
    
    for i in range(nr_experiments):
        if i % 2 == 0:
            case = {uncs[0].name: random.random()}
            result = {outcomes[0].name: np.random.rand(10)}
        else: 
            case = {uncs[1].name: random.random()}
            result = {outcomes[1].name: np.random.rand(10)}
    
        callback(case, policy, name, result)
    
    results = callback.get_results()
    EMAlogging.debug("\n"+str(results[0]))
    for key, value in results[1].iteritems():
        EMAlogging.debug("\n" + str(key) + "\n" + str(value))   

if __name__ == "__main__":
    EMAlogging.log_to_stderr(EMAlogging.DEBUG)
#    test_callback_initalization()
#    test_callback_store_results()
#    test_callback_call_intersection()
    test_callback_call_union()
    