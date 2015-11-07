namespace cloudclient {
	class CCPluginManager {

	private:
		int pluginList;
		Queue resultsQueue;

	public:
		void locate();

		void load();

		void run();

		void registerPlugin();

		void dispatch();

		void getResult();

		void operation();
	};
}
