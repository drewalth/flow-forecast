
generate_clients: clean swift_client typescript_client kotlin_client

swift_client:
	$(MAKE) create_sdk_dir SDK=swift && \
	npx @openapitools/openapi-generator-cli generate \
	-i flow-forecast.openapi.yml \
	-g swift5 \
	-o ./sdks/swift/ \
	--additional-properties projectName=FlowForecast \
	--additional-properties useSPMFileStructure=true \
	--additional-properties useClasses=false \
	--additional-properties useJsonEncodable=false \
	--additional-properties responseAs=AsyncAwait

typescript_client:
	$(MAKE) create_sdk_dir SDK=typescript && \
	npx @openapitools/openapi-generator-cli generate -i flow-forecast.openapi.yml -g typescript-fetch -o ./sdks/typescript/

kotlin_client:
	$(MAKE) create_sdk_dir SDK=kotlin && \
	npx @openapitools/openapi-generator-cli generate -i flow-forecast.openapi.yml -g kotlin -o ./sdks/kotlin/

create_sdk_dir:
	mkdir -p ./sdks/$(SDK)

clean:
	rm -rf ./sdks