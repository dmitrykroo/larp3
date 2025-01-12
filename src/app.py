version: 1
disable_existing_loggers: False

formatters:
  standard:
    format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    formatter: standard
    stream: ext://sys.stdout

  file:
    class: logging.FileHandler
    level: INFO
    formatter: standard
    filename: logs/application.log

loggers:
  nft_valuation_advisor:
    level: DEBUG
    handlers: [console, file]
    propagate: no

root:
  level: WARNING
  handlers: [console]
                        
                        
                        
                        
                        
                       
                       
                       
                       
                       
