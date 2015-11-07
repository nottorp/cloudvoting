namespace cloudclient {
	class CCCommand {

	public:
		int args;
		int commands;
		int name;

		void wait();

		void finished();
	};
}
