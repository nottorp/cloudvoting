namespace cloudclient {
	class CCConnectionManager {

	private:
		cloudclient::CCConnectionQueue queue;
		cloudclient::CCConnection* connection;
		cloudclient::CCPluginManager pluginManager;
		int instance;

	public:
		void run();

		void stop();

	private:
		CCConnectionManager();

	public:
		cloudclient::CCConnectionManager getInstance();
	};
}
