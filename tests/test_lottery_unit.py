from brownie import accounts , Lottery , config , network 
from scripts.deploy_lottery import deploy_lottery
from web3 import Web3 

def test_get_entrance_fee() : 
    # arrange 
    lottery = deploy_lottery()
    # act 
    expected_entrance_fee = Web3.toWei(0.025 , "ether") 
    entrance_fee = lottery.getEntranceFee()
    # assert 
    assert expected_entrance_fee == entrance_fee
    
       
    
