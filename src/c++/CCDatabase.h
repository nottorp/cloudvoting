namespace cloudclient {
	class CCDatabase {

	private:
		int instance;

	public:
		void execute();

		void run();

	private:
		void handleCommands();

		void operation();
	};
}
