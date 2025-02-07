module.exports = {
  apps: [
    {
      name: 'miner',
      interpreter: 'python3',
      script: './neurons/miner.py',
      args: '--netuid 50 --network finney --logging.debug --wallet.name mhhbsj --wallet.hotkey miner0 --axon.port 8091 --blacklist.force_validator_permit true --blacklist.validator_min_stake 1000',
      env: {
        PYTHONPATH: '.'
      },
    },
    {
      name: 'miner3',
      interpreter: 'python3',
      script: './neurons/miner.py',
      args: '--netuid 50 --network finney --logging.debug --wallet.name msgpoj --wallet.hotkey miner1 --axon.port 8094 --blacklist.force_validator_permit true --blacklist.validator_min_stake 1000',
      env: {
        PYTHONPATH: '.'
      },
    },
    {
      name: 'miner4',
      interpreter: 'python3',
      script: './neurons/miner.py',
      args: '--netuid 50 --network finney --logging.debug --wallet.name boss --wallet.hotkey miner0 --axon.port 8095 --blacklist.force_validator_permit true --blacklist.validator_min_stake 1000',
      env: {
        PYTHONPATH: '.'
      },
    },
  ],
};
