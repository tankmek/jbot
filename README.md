# jbot

## BETA

## Prerequisites

`python 3`  
`pip`  
`py3cw`    
`git`  

## Usage

```
git clone https://github.com/tankmek/jbot.git
cd jbot
chmod 700 parrot.py
vim parrot.py
```

Go to 3Commas and create an API key that has Bots Read and Bots Write permissions.
Copy and Paste the API Key and Secret into the corresponding variables:
### api_key
### api_secret

Now save the file and exit the editor.

```
./parrot.py -b | -u <blacklist_file>
-b, --show-blacklist (show blacklist [default])
-u, --update-blacklist (update blacklist)
```

# Notes
The blacklist file should be a list of tokens pairs separated by spaces.

# DEMO

```
bash $ ./parrot.py --show-blacklist
BRL_USDT USDT_BTT USDT_UNIUP USDT_TRXDOWN USDT_BTCUP ETH_CMT USDT_ETH USDT_YFI USDT_XTZUP USDT_ATM USDT_BAL USDT_BCHUP USDT_FLM USDT_LINKUP BTC_TNB USDT_ETHUP USDT_TRXUP USDT_XLMUP USDT_STMX USDT_SUSHIDOWN IDRT_USDT USDT_AAVEUP USDT_EOSUP ZAR_USDT USDT_CHZ USDT_MKR UAH_USDT USDT_BTCDOWN USDT_LTCDOWN USDT_SUSD USDT_ADADOWN ETH_SUSD USDT_ASR BTC_VIBE USDT_XRPUP USDT_XTZDOWN USDT_XRPDOWN USDT_EOSDOWN USDT_DOTUP USDT_BNBDOWN BKRW_USDT USDT_BCH USDT_XRP USDT_SXPDOWN USDT_LTCUP USDT_PAXG USDT_ZRX USDT_ANKR BTC_BCPT USDT_DOTDOWN BVND_USDT USDT_LINKDOWN USDT_OG USDT_BNBUP BTC_XMR BIDR_USDT USDT_TUSD NGN_USDT RUB_USDT USDT_SXPUP USDT_UNIDOWN USDT_EUR USDT_REEF USDT_DOGE USDT_BUSD USDT_STORJ USDT_JUV USDT_USDC USDT_FILDOWN USDT_YFIDOWN USDT_YFIUP USDT_SUSHIUP USDT_BCHDOWN USDT_FILUP USDT_PAX USDT_AUD DAI_USDT USDT_AAVEDOWN USDT_ADAUP BTC_OG USDT_RVN USDT_GBP USDT_ETHDOWN USDT_XLMDOWN

There are 84 pairs in the black list
```
