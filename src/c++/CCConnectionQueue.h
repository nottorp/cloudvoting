namespace cloudclient {
	class CCConnectionQueue {

	private:
		cloudclient::CCConnectionData incoming;
		cloudclient::CCConnectionData outgoing;

	public:
		void put();

		void get();
	};
}
