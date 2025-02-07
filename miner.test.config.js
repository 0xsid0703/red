module.exports = {
  apps: [
    {
      name: 'miner',
      interpreter: 'python3',
      script: './neurons/miner.py',
      args: '--netuid 50 --logging.debug --logging.trace --subtensor.network test --wallet.name mhhbsj --wallet.hotkey miner0 --axon.port 8091 --blacklist.validator.min_stake 0',
      env: {
        PYTHONPATH: '.'
      },
    },
  ],
};
