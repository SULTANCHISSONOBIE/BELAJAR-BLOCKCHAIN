pragma solidity ^0.5.0;

contract helloWorld{
    uint256 totalCoin;

    function addCoin(uint256 nCoin) public{
        totalCoin += nCoin;
    }

    //view; for non transaction (not changing the state on the blockchain (No Gas Needed)
    //rerturn; this function will return data as the result

    function viewTotalCoin() public view returns(uint){
        return totalCoin;
    }
}