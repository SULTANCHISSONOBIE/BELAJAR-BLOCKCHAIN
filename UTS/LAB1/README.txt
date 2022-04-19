# Lab 1 : Deposit / Withdraw Ether

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.1;

contract SendMoneyExample {
    uint public balanceReceived;
    function receiveMoney() public payable {
        balanceReceived += msg.value;
    }
 
    function getBalance() public view returns(uint) {
        return address(this).balance;
    }
}
```

## Screenshots

![App Screenshot](https://github.com/SULTANCHISSONOBIE/BELAJAR-BLOCKCHAIN/blob/main/UTS/LAB1/Documentation/Picture1.png)

Penjelasan per line
uint public balanceReceived : adalah variable penyimpanan umum / public. Variabel public akan membuat fungsi pengambil secara otomatis di Solidity. Jadi developer selalu dapat memonitor konten yang sedang ada pada variable tersebut.
balanceReceived += msg.value : msg adalah objek global yang selalu ada yang berisi beberapa informasi tentang transaksi yang sedang berlangsung. Property yang paling penting disini adalah .value dan .sender. 
function getBalance() public view returns(uint) : fungsi view adalah fungsi yang tidak mengubah penyimpanan (read-only) dan dapat mengembalikan informasi. Tidak perlu ditambang.
address(this).balance : variable dari tipe alamat selalu memiliki property yang disebut .balance yang memberi sejumlah Ether yang disimpan di alamat tersebut. Hal ini bukan berarti kita dapat mengakses secara mudah, namun hanya memberitahu berapa banyak yang disimpan disana. address(this) mengonversi Smart Contract ke alamat. Jadi, line ini pada dasarnya mengembalikan jumlah Ether yang disimpan di Smart Contract itu sendiri.

