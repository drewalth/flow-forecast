pretty:
	swiftformat . --config airbnb.swiftformat

setup: install_homebrew install_nvm nvm_lts install_node_deps install_swiftformat

install_homebrew:
    @which brew || /bin/bash -c "$$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

install_nvm:
	@which nvm || brew install nvm

nvm_lts: install_homebrew install_nvm
	@source $(HOME)/.nvm/nvm.sh && \
	nvm install --lts && \
	nvm use --lts && \
	nvm alias default node
	
install_node_deps: nvm_lts
	npm install

install_swiftformat: install_homebrew
	@which swiftformat || brew install swiftformat